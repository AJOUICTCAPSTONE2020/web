import React, { Component } from 'react';
import Header from '../layout/Header';
import Search from './Search';

class SelectChapter extends Component {
    constructor(props) {
        super(props);
        this.state = {
            TwitchData: [],
            TwitchChapter: [],
        }
    }

    callApi1 = () => {

        fetch("http://127.0.0.1:8000/api/TwitchData/1")
        

        .then(res => res.json())

        .then(json => this.setState({
            TwitchData: json,
        }));
        
    }

    callApi2 = () => {

        fetch("http://127.0.0.1:8000/api/TwitchChapter/1")
        

        .then(res => res.json())

        .then(json => this.setState({
            TwitchChapter: json,
            
        }));
        
    }

    componentDidMount() {
    
        this.callApi1();
        this.callApi2();
    }

    render() {
        const {params} = this.props.match;
        var Chapter = this.state.TwitchChapter;
        var Data = this.state.TwitchData;
   
        console.log(Chapter);
        console.log(Data);

        const x=[];
        const y=[];
        for (var i in Data){
            x.push(Data[i].title)
            y.push(Data[i].name)
        }
        
        const a=[];
        const b=[];
        for (var i in Chapter){
            a.push(Chapter[i].chaptername)
            b.push(Chapter[i].chaptertime)
        }
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
                                
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    {x}
                                </td>
                                <td>
                                    {y}
                                </td>
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

                <div>
                    {a}{b}
                </div>
            </html>
        );
    }
}

  export default SelectChapter;