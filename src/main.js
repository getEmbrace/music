import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { Button, Select, Slider, Row, Col } from 'element-ui';

Vue.config.productionTip = false

Vue.component(Button.name, Button);
Vue.component(Select.name, Select);

Vue.use(Slider)
Vue.use(Row)
Vue.use(Col)

Vue.prototype.$bus = new Vue()

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
