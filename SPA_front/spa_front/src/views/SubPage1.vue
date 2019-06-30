<template>
  <div class='sub_page1'>
    <HelloWorld style="width:80%;margin:auto;margin-top:2rem" :nowArray='data' />
    <el-button  type="primary" plain @click='post_data_2' style="margin-top:3rem">存储当前数据</el-button>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import config from '@/../config/config.ts';

@Component({
  components: {
    HelloWorld,
  },
})
export default class SubPage1 extends Vue {
  private data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ];
  private timer: any;
  private get_data_1() {
    this.$axios({
      method: 'get',
      url: config.baseURL + '/data/get_array',
    }).then((res) => {
      if (res.data.code === '200') {
        this.data = res.data.data;
      }
    });
  }

  private post_data_2() {
    this.$axios({
      method: 'post',
      url: config.baseURL + '/data/post_array',
      data: {
        array: JSON.stringify(this.data),
      },
    }).then((res) => {
      return;
    });
  }

  private mounted() {
    this.get_data_1();
    this.timer = setInterval(this.get_data_1, 10000);
  }
  private destory() {
    clearInterval(this.timer);
  }
}
</script>
