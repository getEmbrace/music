<template>
  <div class="songList">
    <div class="back" @click="back_click">
      <i class="el-icon-back"></i>
    </div>
    <div class="banner_l">
      <div class="mask" :class="{mask_active: isActive}"></div>
      <div class="shoucang" @click="shoucang_click">
        <span>收藏</span>
      </div>
      <div class="search" @click="search_click">
        <span>发现</span>
      </div>
    </div>
    <div class="showList_sc"  v-show="!isActive">
      <ShowList v-if="this.$store.state.songCollect.length != 0"></ShowList>
      <div class="empty" v-else>
        <img src="~assets/img/empty.gif" alt="">
      </div>
    </div>
    <SongSearch v-show="isActive"></SongSearch>
  </div>
</template>

<script>
import ShowList from './child/ShowList.vue'
import SongSearch from './child/SongSearch.vue'

export default {
  name: "SongList",
  components: {
    ShowList,
    SongSearch
  },
  data(){
    return {
      isActive: false
    }
  },
  methods: {
    shoucang_click(){
      this.isActive = false;
    },
    search_click(){
      this.isActive = true;
    },
    back_click(){
      this.$emit("back_click")
    }
  }
}
</script>

<style>
.mask_active {
  right: 0;
}
.songList {
  position: fixed;
  bottom: 0;
  width: 100vw;
  height: 70vh;
  border-radius: 20px 20px 0 0;
  background-color: #fff;
  z-index: 2000;
}
.songList .back {
  position: absolute;
  width: 50px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  font-size: 29px;
  color: rgba(0, 0, 0, 0.548);
}
.banner_l {
  position: relative;
  display: flex;
  justify-content: space-between;
  margin: 10px auto;
  width: 40vw;
  height: 28px;
}
.banner_l .shoucang {
  width: 50%;
  height: 100%;
  border-radius: 30px;
  text-align: center;
  line-height: 28px;
  font-size: 19px;
  color: rgb(26, 25, 25);
}
.banner_l .search {
  width: 50%;
  height: 100%;
  border-radius: 30px;
  text-align: center;
  line-height: 28px;
  font-size: 19px;
  color: rgb(31, 30, 30);
}
.banner_l .mask {
  position: absolute;
  width: 50%;
  height: 100%;
  border-radius: 30px;
  z-index: -1;
  background-color: #409eff;
}
.showList_sc {
  height: calc(70vh - 50px);
  overflow: auto;
}
.showList_sc .empty {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #F7F7F7;
  overflow: hidden;
}
.showList_sc .empty img{
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 100vw;
  transform: translate(-30%);
  font-size: 50px;
}
</style>