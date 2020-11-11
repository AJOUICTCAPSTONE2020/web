import React, { Component } from 'react';
import Header from '../layout/Header';

class SelectChapter extends Component {

    render() {
        const {params} = this.props.match;
        
        return (
            <html>
                <Header></Header>
              
                <div id="twitchVideo">
                    <iframe src={`https://player.twitch.tv/?video=${params.value}&parent=127.0.0.1`}
                    allowfullscreen="true" 
                    scrolling="no" 
                    height="378" 
                    width="620"
                    ></iframe>
                </div>
                <div id="videoInfo">
                    <table id="twitchVideoInfo">
                        <thead>
                            <tr>
                                <th width="300">Title</th>
                                <th width="180">Streamer</th>
                                <th width="180">Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>컴퓨터 싹 바꾼 방송</td>
                                <td>빅헤드</td>
                                <td>2020-10-21</td>
                            </tr>
                        </tbody>
                    </table>
          
                </div>
                <div id="chapter">
                    <h4 id="selectdsc"> 하이라이트 분석을 할 챕터를 선택하세요!</h4>
                    <ul id="chapterList">
                        <button class="ChapterButton"> Just chatting <br></br> 2시간 3분 </button>
                        <button class="ChapterButton"> League of legends <br></br> 4시간 43분 </button>
                        <button class="ChapterButton"> Squad <br></br> 2시간 16분 </button>
                    </ul>
                </div>
            </html>
        );
    }
}

  export default SelectChapter;