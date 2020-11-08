import React, { Component } from 'react';

class HighlightResult extends Component {
    state={
        boards:[
            {
                brdNo:1,
                time: "0:30:10",
                senti: "Joy",
            },
            {
                brdNo:2,
                time: "1:10:24",
                senti: "Joy",
            },
            {
                brdNo:3,
                time: "1:45:55",
                senti: "Surprise",
            },
            {
                brdNo:4,
                time: "2:12:48",
                senti: "Joy",
            },
            {
                brdNo:5,
                time: "3:34:09",
                senti: "Teasing",
            }

        ]
    }
    render() {
        const { boards } = this.state;
        return (
            <html>
                <div id="twitchVideo">
                    <iframe src="https://player.twitch.tv/?video=777124743&parent=localhost" 
                    frameborder="0" 
                    allowfullscreen="true" 
                    scrolling="no" 
                    height="378" 
                    width="620"
                    ></iframe>
                </div>

                <div id="highlightResult">
                        <h3> 하이라이트 추출 결과  </h3>
                        <h5 id="highlightdsc"> 하이라이트 구간을 클릭하면 해당 타임라인으로 이동합니다!</h5>
                        <br></br>
                        <table id="highlightTable" border="2">
                            <tbody>
                                <tr align="center">
                                    <td> No. </td>
                                    <td> 하이라이트 구간 </td>
                                    <td> 감성분석 결과 </td>
        
                                </tr>
                                {
                                    boards.map(row => 
                                        (<BoardItem key={row.brdno} row={row} />)
                                    )
                                }
                            </tbody>
                        </table> 
                    </div>

            </html>
        );
    }
}

class BoardItem extends React.Component { 
    render() { 
        return( 
            <tr> 
                <td width="50" height="40">{this.props.row.brdNo}</td> 
                <td width="300" height="40">{this.props.row.time}</td> 
                <td width="150" height="40">{this.props.row.senti}</td> 
              
            </tr> 
        ); 
    } 
}

  export default HighlightResult;