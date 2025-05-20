import { Ref } from 'vue';
import axiosInstance from './getCards';
import { useCarddata } from '@/stores/carddata';
import { isloading } from '@/stores/isloading';

interface ScrollOptions {
  scrollContainer: Ref<HTMLElement | null>;
  dataloading: Ref<boolean>;
  cardstore: ReturnType<typeof useCarddata>;
  isloadingstore: ReturnType<typeof isloading>;
}

export const useInfiniteScroll = (options: ScrollOptions) => {
  const { scrollContainer, dataloading, cardstore, isloadingstore } = options;

  // 刷新卡片
  const refresh = (path: string, api: string, category: string) => {
    console.log(`刷新分类: ${category}, 路径: ${path}, API: ${api}`);
    cardstore.carddata.splice(0, cardstore.carddata.length); // 清空列表
    isloadingstore.dataloading = true;
    dataloading.value = true;
    cardstore.category = category;
    isloadingstore.dataend = false;

    axiosInstance.post(api, { skip: 0, category: category })
      .then((response) => {
        const receivedCards = response.data.data;
        if (receivedCards && Array.isArray(receivedCards)) {
          cardstore.carddata.push(...receivedCards);
          console.log(`分类 "${category}" 的初始卡片数据已加载:`, cardstore.carddata);
          if (receivedCards.length < 5) {
            console.log("分类", category, "的卡片数据不足5条，已设置为已结束。")
            isloadingstore.dataend = true;
          }
        } else {
          console.warn(`分类 "${category}" 返回的初始卡片数据无效或为空:`, receivedCards);
        }
      })
      .catch(error => {
        console.error(`从 ${api} (分类: ${category}) 刷新初始数据失败:`, error);
      })
      .finally(() => {
        dataloading.value = false;
      });
  };

  // 加载更多数据
  const loadMore = async () => {
    dataloading.value = true;
    try {
      const currentItemCount = cardstore.carddata.length;
      console.log(`请求下一页，跳过: ${currentItemCount}`);

      const response = await axiosInstance.post('/getcard', { 
        skip: currentItemCount,
        category: cardstore.category 
      });
      const receivedCards = response.data.data;

      if (receivedCards && Array.isArray(receivedCards)) {
        cardstore.carddata.push(...receivedCards);
        console.log('已添加数据：', receivedCards);
        console.log('目前总卡片数据：', cardstore.carddata);
        if (receivedCards.length === 0) {
          isloadingstore.dataend = true;
        }
      } else {
        console.log('未收到卡片数据或格式不正确。', receivedCards);
      }
    } catch (error) {
      console.error('请求失败:', error);
    } finally {
      dataloading.value = false;
    }
  };

  // 滚动事件处理
  const handleScroll = () => {
    if (!scrollContainer.value) return;
    const scrollTop = scrollContainer.value.scrollTop;
    const clientHeight = scrollContainer.value.clientHeight;
    const scrollHeight = scrollContainer.value.scrollHeight;
    if (scrollTop + clientHeight >= scrollHeight - 10) {
      onScrollToBottom();
    }
  };

  // 滚动到底部处理
  const onScrollToBottom = () => {
    if (isloadingstore.dataend || dataloading.value) {
      return;
    }
    console.log("滚动到底部了！准备延时加载...");
    dataloading.value = true;
    setTimeout(() => {
      if (dataloading.value && !isloadingstore.dataend) {
        console.log("延时结束，开始获取下一页数据...");
        loadMore();
      } else {
        console.log("延时期间加载状态改变，取消本次数据获取。");
        if (dataloading.value) dataloading.value = false;
      }
    }, 1000);
  };

  return {
    refresh,
    handleScroll,
    loadMore
  };
}; 