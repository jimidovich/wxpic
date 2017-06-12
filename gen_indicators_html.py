import os


html = '''
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="Author" content="qcy">
        <meta name="Keywords" content="tech indicator">
        <meta name="Description" content="buy sell tips">
        <title>技术指标</title>
    </head>

    <link rel="stylesheet" href="./tech.css" type="text/css">




    <script>
	   // 对Date的扩展，将 Date 转化为指定格式的String
	   // 月(M)、日(d)、小时(h)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符，
	   // 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字)
	   // 例子：
	   // (new Date()).Format("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423
	   // (new Date()).Format("yyyy-M-d h:m:s.S")      ==> 2006-7-2 8:9:4.18
	   Date.prototype.Format = function(fmt) { //author: meizz
		     var o = {
			       "M+" : this.getMonth() + 1, //月份
			       "d+" : this.getDate(), //日
			       "h+" : this.getHours(), //小时
			       "m+" : this.getMinutes(), //分
			       "s+" : this.getSeconds(), //秒
			       "q+" : Math.floor((this.getMonth() + 3) / 3), //季度
			       "S" : this.getMilliseconds()
		         //毫秒
		     };
		     if (/(y+)/.test(fmt))
			       fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "")
					       .substr(4 - RegExp.$1.length));
		     for ( var k in o)
			       if (new RegExp("(" + k + ")").test(fmt))
				         fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k])
						                     : (("00" + o[k]).substr(("" + o[k]).length)));
		     return fmt;
	   };
	   var time1 = new Date().Format("yyyy/MM/dd");
	   var dateTime = new Date().Format("yyyy/MM/dd hh:mm:ss");

	   /*document.write(dateTime);*/
    </script>


    <script type="text/javascript">
	   var t = null;
	   function time() {
		     var dateTime = new Date().Format("yyyy/MM/dd hh:mm:ss");
		     document.getElementById("timeShow").innerHTML = dateTime;
		     t = setTimeout(time, 1000);
	   }
	   window.onload = function() {
		     time();
	   };
    </script>


    <body>
'''

html2 = '''

	      <div style="margin: 0 0px; background-color: white;">

		        <div style="margin-left: 55px;">
			          <!-- <span class="arial_17">欧元兑美元&nbsp;EURUSD</span> -->
			          <span style="font-size:17px; text-align:center">欧元兑美元&nbsp;EURUSD</span>
                <span title="Euro Zone" class="ceFlags Europe">&nbsp;</span>
		        </div>

		        <div style="margin-top: 8px;">
			          <!-- 说明：下跌时候，箭头要用up，因为中国和外国的颜色是反的 -->
			          <div style="margin-left: 0px;">
				            <span class="upArrow" style="float: left;">
					              <!--Down-->
				            </span>
				            <span class="inlineblock">

					              <span class="top bold inlineblock" style="float: left; margin-top: 5px;">

						                <span class="arial_13">1.0855</span>
                            <span class="arial_13 greenFont" style="margin-left:1px;">-0.14</span>
						                <!-- <span dir="rtl"></span> -->
                            <span class="arial_13 greenFont  pid-166-pcp parentheses">-0.37%</span>
					                  <!-- </div> -->
					                  <span class="bottom lighterGrayFont arial_11" style="margin-left: -154px;margin-top: 31px; float: left;"></span>
					                  <!-- <span class="inlineblock greenClockBigIcon" style=""></span> -->
                            <span id="timeShow" class="bold" style="margin-left: 3px; font-size: 10px">这里显示时间</span>
					              </span>
				            </span>
			          </div>
		        </div>
	      </div>

	      <div class="halfSizeColumn" style="margin-top: -30px;">
		        <h3>
			          <a href="#">&nbsp;移动平均 MA</a><span
				                                             class=" arial_11 bold lighterGrayFont h3TitleDate"> </span>
		        </h3>

		        <div class="clear"></div>
		        <table class="genTbl closedTbl movingAvgsTbl" id="curr_table">
			          <thead>
				            <tr>
					              <th class="first left">周期</th>
					              <th>简单均线&nbsp;SMA</th>
					              <th>指数均线&nbsp;EMA</th>
				            </tr>
			          </thead>
			          <tbody>
				            <tr>
					              <td class="first left symbol">MA5</td>
					              <td>{ma5}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
					              <td>{ema5}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">MA10</td>
					              <td>{ma10}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
					              <td>{ema10}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">MA20</td>
					              <td>{ma20}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
					              <td>{ema20}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">MA50</td>
					              <td>{ma50}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
					              <td>{ema50}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">MA100</td>
					              <td>{ma100}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
					              <td>{ema100}&nbsp; <span class="greenFont bold"> 偏空 </span>
					              </td>
				            </tr>
				            <tr>
					              <td colspan="3" class="first left lastRow">
						                <p class="inlineblock">
							                  <span class="noBold">偏多:</span> <span>0</span>
						                </p>
						                <p class="inlineblock">
							                  <span class="noBold">偏空:</span> <span>12</span>
						                </p> <br>
						                <p class="inlineblock">
							                  综合研判：<span class="greenFont bold uppercaseText"> {shit} </span>
						                </p>
					              </td>
				            </tr>
			          </tbody>
		        </table>
	      </div>



	      <div class="halfSizeColumn tech_indicator_div"
		                style="margin-top: -20px;">
		        <h3>
			          <a href="#">&nbsp;技术指标</a><span
				                                          class=" arial_11 bold lighterGrayFont h3TitleDate"> </span>
			          <!-- 这里可以写点什么 -->

		        </h3>
		        <span class="clear"></span>
		        <table class="genTbl closedTbl movingAvgsTbl float_lang_base_2"
			                    id="curr_table">
			          <thead>
				            <tr>
					              <th class="first left">指标</th>
					              <th>数值</th>
					              <th class="left textNum">诊断</th>
				            </tr>
			          </thead>
			          <tbody>
				            <tr>
					              <td class="first left symbol">MACD(12,26,9)</td>
					              <td class="right">{macd}</td>
					              <td class="left textNum bold"><span class="greenFont bold">偏空</span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">RSI(14)</td>
					              <td class="right">{rsi}</td>
					              <td class="left textNum bold"><span class="bold">超卖</span></td>
				            </tr>
				            <tr>
					              <td class="first left symbol">ADX(14)</td>
					              <td class="right">{adx}</td>
					              <td class="left textNum bold"><span class="bold">超卖</span></td>
				            </tr>
				            <tr>
					              <td class="first left symbol">STOCH(9,6)</td>
					              <td class="right">{stoch}</td>
					              <td class="left textNum bold"><span class="bold">超卖</span></td>
				            </tr>
				            <tr>
					              <td class="first left symbol">CCI(14)</td>
					              <td class="right">{cci}</td>
					              <td class="left textNum bold"><span class="greenFont bold">偏空</span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">Williams %R</td>
					              <td class="right">{willr}</td>
					              <td class="left textNum bold"><span class="greenFont bold">偏空</span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">Ultimate Oscillator</td>
					              <td class="right">{uo}</td>
					              <td class="left textNum bold"><span class="greenFont bold">偏空</span>
				            </tr>
				            <tr>
					              <td class="first left symbol">ROC</td>
					              <td class="right">{roc}</td>
					              <td class="left textNum bold"><span class="greenFont bold">偏空</span></td>
				            </tr>
				            <tr>
					              <td class="first left symbol">SAR</td>
					              <td class="right">{sar}</td>
					              <td class="left textNum bold"><span class="greenFont bold">偏空</span>
					              </td>
				            </tr>
				            <tr>
					              <td class="first left symbol">ATR(14)</td>
					              <td class="right">{atr}</td>
					              <td class="left textNum bold"><span class="bold">高波动</span></td>
					              </td>
				            </tr>
				            <tr>
					              <td colspan="3" class="first left lastRow">
						                <p class="inlineblock">
							                  <span class="noBold">偏多:</span> <span>0</span>
						                </p>
						                <p class="inlineblock">
							                  <span class="noBold">偏空:</span> <span>8</span>
						                </p>
						                <p class="inlineblock">
							                  <span class="noBold">中性:</span> <span>0</span>
						                </p> <br>
						                <p class="inlineblock">
							                  综合研判：<span class="greenFont bold uppercaseText"> {shit2} </span>
						                </p>
					              </td>
				            </tr>
			          </tbody>
		        </table>
	      </div>
    </body>
</html>
'''


# data = {'ma5':1111, 'ema5':12313, 'shit':'空头抛压极强', 'shit2':'blablabla'}


def gen_html_pic(data, filename):
    with open('./{}.html'.format(filename), 'w') as f:
        f.write(html + html2.format(**data))

    html_url = 'file:///home/yiju/wxpic/{}.html'.format(filename)

    os.system('CutyCapt --url={} --out={}.png --min-width=100 --min-height=10 --zoom-factor=2.0'.format(html_url, filename))
