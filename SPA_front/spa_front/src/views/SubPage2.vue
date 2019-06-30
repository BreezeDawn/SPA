<template>
  <div id='sub_page1'>
    <div id="chart"></div>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import config from '@/../config/config.ts';
import HighCharts from 'highcharts';

export default class SubPage2 extends Vue {
  private option = {
    title: {
      text: 'SubPage 2 Data',
    },
    subtitle: {
      text: '数据来源：127.0.0.1:7777',
    },
    yAxis: {
      title: {
        text: '数值',
      },
    },
    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
    },
    plotOptions: {
      series: {
        label: {
          connectorAllowed: false,
        },
        pointStart: 1,
      },
    },
    series: [{
      name: '数位',
      data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    }],
    responsive: {
      rules: [{
        condition: {
          maxWidth: 500,
        },
        chartOptions: {
          legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
          },
        },
      }],
    },
  };

  private mounted() {
    this.init_charts(this.option);
  }

  private get_db_two() {
    this.$axios({
      method: 'get',
      url: config.baseURL + '/data/get_db_two',
    }).then((res) => {
      if (res.data.code === '200') {
        console.log(res.data.data);
      }
    });
  }

  private init_charts(option: any) {
    HighCharts.chart('chart', option);
  }
}
</script>