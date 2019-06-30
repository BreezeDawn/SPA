<template>
  <div class="sub_page2">
    <h1>This is an about page</h1>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import config from '@/../config/config.ts';

@Component({
  components: {
    HelloWorld,
  },
})
export default class SubPage1 extends Vue {
  private data = [];

  private get_data_2() {
    this.$axios({
      method: 'get',
      url: config.baseURL + '/data/get_db_two',
    }).then((res) => {
      if (res.data.code === '200') {
        this.data = res.data.data;
        console.log(this.data);
      }
    });
  }

  private mounted() {
    this.get_data_2();
  }
}
</script>