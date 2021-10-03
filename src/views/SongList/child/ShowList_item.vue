<template>
  <div class="showListItem">
    <div class="order">
      <slot name="order" v-if="!isSonging"></slot>
      <img v-else :src="$store.state.songInfo.pic" alt="" />
    </div>
    <div class="songInfo_s" @click="songItem_click">
      <div class="songName" :class="{ style_songing: isSonging }">
        <slot name="songName"></slot>
      </div>
      <div class="author" :class="{ style_songing: isSonging }">
        <slot name="author"></slot>
      </div>
    </div>
    <div class="del_s" @click="del_s_click">
      <i class="el-icon-delete" v-if="!isSearch"></i>
      <div class="img" v-else>
        <img v-if="isSoucang_active" src="~assets/icon/shoucang.png" alt="" />
        <img v-else src="~assets/icon/shoucang_active.png" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ShoeListItem",
  props: {
    songItem: {
      type: Object,
      default: () => {
        return {};
      },
    },
    isSearch: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isSonging: false,
      isSoucang_active: true,
    };
  },
  computed: {
    //监听 this.$store.state.songInfo.id 变化
    songingId() {
      return this.$store.state.songInfo.id;
    },
  },
  watch: {
    //监听 this.$store.state.songInfo.id 变化
    songingId() {
      this.initSonging()
    },
  },
  methods: {
    del_s_click() {
      if (!this.isSearch) {
        this.$emit("del_s_click", this.songItem.id);
        this.$bus.$emit('resetSoucang_s')
      } else {
        //检查是否已收藏
        let isCollect = false;
        this.$store.state.songCollect.forEach((el) => {
          if (this.songItem.id == el.id) {
            isCollect = true;
            return;
          }
        });
        let name = this.songItem.name;
        let ar = this.songItem.ar;
        let id = this.songItem.id;
        //是否应该加入收藏
        if (this.isSoucang_active && isCollect == false) {
          this.$store.commit("pushItem_songCollect", { name, ar, id });
        } else if (!this.isSoucang_active && isCollect == true) {
          this.$store.commit("delItem_songCollect", id);
        }
        //是否收藏之前正在播放
        if(this.songItem.id == this.$store.state.songInfo.id){
          this.$bus.$emit('resetSoucang')
        }
        this.isSoucang_active = !this.isSoucang_active;
      }
    },
    songItem_click() {
      if (
        this.songItem.id != this.$store.state.songInfo.id ||
        this.$store.state.songInfo.status == false
      ) {
        this.$store.commit("setSongInfo_id", this.songItem.id);
        this.$store.commit("setSongInfo_name", this.songItem.name);
        this.$store.commit("setSongInfo_ar", this.songItem.ar);
        this.$bus.$emit("getSongInfoById", this.songItem.id);
      }
    },
    initSoucang() {
      //检查是否已收藏
      let isCollect = false;
      this.$store.state.songCollect.forEach((el) => {
        if (this.songItem.id == el.id) {
          isCollect = true;
          return;
        }
      });
      if (isCollect) {
        this.isSoucang_active = false;
      } else {
        this.isSoucang_active = true;
      }
    },
    initSonging(){
      if (this.songItem.id == this.$store.state.songInfo.id) {
        this.isSonging = true;
      } else {
        this.isSonging = false;
      }
    }
  },
  mounted() {
    this.initSoucang();
    this.initSonging();
    this.$bus.$on('resetSoucang_s', ()=> {
      this.initSoucang();
    })
  },
};
</script>

<style>
.style_songing {
  color: #409eff !important;
}
.showListItem {
  display: flex;
  width: 100%;
  height: 50px;
}
.showListItem .order {
  width: 50px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  color: rgb(22, 22, 22);
  font-size: 20px;
}
.showListItem .order img {
  width: 40px;
  height: 40px;
  margin-top: 5px;
  border-radius: 50%;
}
.showListItem .songInfo_s {
  flex: 1;
}
.songInfo_s .songName {
  width: 100%;
  height: 50%;
  line-height: 25px;
  color: rgb(22, 22, 22);
  overflow: hidden;
  font-size: 20px;
}
.songInfo_s .author {
  width: 100%;
  height: 50%;
  border-bottom: 1px solid rgba(0, 0, 0, 0.116);
  line-height: 25px;
  color: rgb(114, 114, 114);
  font-size: 16px;
}
.showListItem .del_s {
  width: 50px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  font-size: 20px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.116);
}
.showListItem .del_s img {
  width: 27px;
  height: 27px;
  margin-top: 9px;
}
</style>