import React, { Component } from 'react';
import Header from '../layout/Header';

class HighlightResult extends Component {
    constructor(props) {
		super(props);
		this.state = {
            result: [],
            TwitchData:[],
            downloadState: false,
        };
       
    }

    callApi1 = () => {

        fetch('http://127.0.0.1:8000/api/selectchapter/' + this.props.match.params.value)
        

        .then(res => res.json())

        .then(json => this.setState({
            TwitchData: json,
        }));
        
    }
    componentDidMount() {
        setInterval(()=> {
            this.callApi1();
            console.log("@@@");
            console.log(this.state.TwitchData);
            console.log(this.state.TwitchData[0].downloadState);
        },5000);

    }
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
                
                <div id="highlightResult">
                        <h3> 하이라이트 추출 결과  </h3>
                        <h5 id="highlightdsc"> 하이라이트 구간을 클릭하면 해당 타임라인으로 이동합니다!</h5>
                        <br></br>
  
                </div>
      

            </html>
        );
    }
}


export default HighlightResult;