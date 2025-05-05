// src/stores/userlogin.ts
import { defineStore } from 'pinia';
import { reactive, ref} from 'vue';
import type { UserInfo } from '../types/userInfo';
export const useCounterStore = defineStore('user', () => {
  const userInfo = reactive<UserInfo>({
    username: '',
  });
  let loading = ref<boolean>(false);
  let homepage = ref<string>('login')
  const alert_sucess = ref<boolean>(false);
  const alert_error = ref<boolean>(false);
  const alert_message = ref<boolean>(false);
  const alert_info = ref<boolean>(false);
  let is_login = ref<boolean>(false)
  console.log("is_login:::::",is_login)
  return {
    userInfo,
    alert_sucess,
    alert_error,
    alert_message,
    alert_info,
    is_login,
    homepage,
    loading,
  };
});
