import { useEventListener } from '@vueuse/core'
import { ref } from 'vue'

export function useKeyboardPaste() {
  const pastedImages = ref<string[]>([])

  // 监听 paste 事件
  useEventListener(document, 'paste', (e: ClipboardEvent) => {
    if (!e.clipboardData) return
    for (const item of e.clipboardData.items) {
      if (item.type.startsWith('image/')) {
        const file = item.getAsFile()
        if (file) {
          const url = URL.createObjectURL(file)
          pastedImages.value.push(url)
        }
      }
    }
  })

  const clearImages = () => {
    pastedImages.value.forEach(url => URL.revokeObjectURL(url))
    pastedImages.value = []
  }

  return {
    pastedImages,
    clearImages
  }
} 