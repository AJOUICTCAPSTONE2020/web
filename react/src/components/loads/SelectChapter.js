import React, { Component } from 'react';
import Header from '../layout/Header';
import Search from './Search';

class SelectChapter extends Component {
    constructor(props) {
        super(props);
        this.state = {
            TwitchData: [],
            TwitchChapter: [],
            value:'',
        };
        this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
		this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        event.preventDefault();
    
        this.props.history.push('/statistics'+'/'+this.state.value)
    }

    callApi1 = () => {

        fetch('http://127.0.0.1:8000/api' + this.props.match.url)
        

        .then(res => res.json())

        .then(json => this.setState({
            TwitchData: json,
        }));
        
    }

    callApi2 = () => {

        fetch('http://127.0.0.1:8000/api/chapter' + this.props.match.url)
        

        .then(res => res.json())

        .then(json => this.setState({
            TwitchChapter: json,
            
        }));
        
    }

    componentDidMount() {
        setTimeout(function() { 
            this.callApi1();
            this.callApi2();
        }.bind(this), 10000)
    }


    render() {
        const {params} = this.props.match;
 
        
        var Chapter = this.state.TwitchChapter;
        var Data = this.state.TwitchData;

        const x=[];
        const y=[];
        for (var i in Data){
            x.push(Data[i].title)
            y.push(Data[i].name)
        }
        console.log(a);
        console.log(b);
        console.log('http://127.0.0.1:8000/api/chapter' + this.props.match.url);
        const a=[];
        const b=[];
        const list=[];
        for (var i in Chapter){
            a.push(Chapter[i].chaptername)
            b.push(Chapter[i].chaptertimme)
            //list.push([Chapter[i].chaptername,Chapter[i].chaptertime])
            list.push(Chapter[i].chaptername)
        }






        const chapterList = list.map(
            
            (name, index) => (<button key={index} class="ChapterButton"> {name} </button>)
        )
        
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
                    {/*
                    <form action="/statistics" method="POST" onSubmit={this.handleSubmit}>
                    
                        <button class="ChapterButton" value={params.value} onClick={this.handleChange}> Just chatting <br></br> 2시간 3분 </button>
                        <button class="ChapterButton" value={params.value} onClick={this.handleChange}> League of legends <br></br> 4시간 43분 </button>
                        <button class="ChapterButton" value={params.value} onClick={this.handleChange}> Squad <br></br> 2시간 16분  </button>
                    </form>
                    */}
                    {chapterList}
                </div>

            </html>
        );
    }
}

  export default SelectChapter;