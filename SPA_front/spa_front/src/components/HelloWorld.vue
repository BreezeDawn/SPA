<template>
  <div>
    <div id='charts'></div>
  </div>
</template>

<script lang='ts'>
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
import HighCharts from 'highcharts';

@Component
export default class HelloWorld extends Vue {
  @Prop() private nowArray!: any;

  private option = {
    chart: {
      type: 'area',
    },
    title: {
      text: 'SubPage 1 Data',
    },
    subtitle: {
      text:
        '数据来源: <a href="http://127.0.0.1:7777/data/get_array">' +
        '127.0.0.1:7777</a>',
    },
    tooltip: {
      pointFormat: '{series.name} number <b>{point.y:,.0f}</b>',
    },
    plotOptions: {
      area: {
        pointStart: 1,
        marker: {
          enabled: false,
          symbol: 'circle',
          radius: 2,
          states: {
            hover: {
              enabled: true,
            },
          },
        },
      },
    },
    series: [
      {
        name: 'ten seconds ago',
        data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      },
      {
        name: 'now',
        data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      },
    ],
  };

  @Watch('nowArray')
  private onArrayChanged(val: any, oldVal: any) {
    const newOption = this.option;
    newOption.series[0].data = oldVal;
    newOption.series[1].data = val;
    this.init_charts(newOption);
  }

  private mounted() {
    this.init_charts(this.option);
  }

  private init_charts(option: any) {
    HighCharts.chart('charts', option);
  }
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped lang='less'>
</style>
