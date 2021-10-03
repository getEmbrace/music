import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    songWord: [],
    songInfo: {
      name: "火羊瞌睡了",
      id: 1436709403,
      ar: "夏天的风",
      pic: "",
      songUrl: "",
      status: false //是否正在播放
    },
    songCollect: [
      {
        name: "处处吻",
        ar: "杨千嬅",
        id: 1360515268
      },
      {
        ar: "火羊瞌睡了",
        id: 1436709403,
        name: "夏天的风",
      }]
  },
  mutations: {
    setSongWord(state, payload) {
      state.songWord = payload
    },
    setSongInfo_status(state, payload) {
      state.songInfo.status = payload
    },
    setSongInfo_name(state, payload) {
      state.songInfo.name = payload
    },
    setSongInfo_id(state, payload) {
      state.songInfo.id = payload
    },
    setSongInfo_ar(state, payload) {
      state.songInfo.ar = payload
    },
    setSongInfo_pic(state, payload) {
      state.songInfo.pic = payload
    },
    setSongInfo_songUrl(state, payload) {
      state.songInfo.songUrl = payload
    },
    pushItem_songCollect(state, payload) {
      state.songCollect.push(payload)
    },
    delItem_songCollect(state, payload) {
      for (let i in state.songCollect) {
        if (state.songCollect[i].id == payload) {
          state.songCollect.splice(i, 1)
        }
      }
    }
  },
  actions: {
  },
  modules: {
  }
})
