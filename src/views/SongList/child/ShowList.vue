<template>
  <div class="showList">
    <ShowListItem
      v-for="(item, index) of songData"
      :key="item.id"
      :songItem="item"
      :isSearch="isSearch"
      @del_s_click="del_s_click($event)"
    >
      <span slot="order">{{ index + 1 }}</span>
      <span slot="songName">{{ item.name }}</span>
      <span slot="author">{{ item.ar }}</span>
    </ShowListItem>
  </div>
</template>

<script>
import ShowListItem from "./ShowList_item.vue";
export default {
  name: "ShowList",
  props: {
    songData: {
      type: Array,
      default(){
        return this.$store.state.songCollect
      }
    },
    isSearch: {
      type: Boolean,
      default: false
    }
  },
  components: {
    ShowListItem,
  },
  methods: {
    del_s_click(songId){
      this.$store.commit('delItem_songCollect', songId)
      this.$bus.$emit('resetSoucang')
    }
  }
};
</script>

<style>
.showList {
  height: 100%;
  overflow: auto;
}
</style>