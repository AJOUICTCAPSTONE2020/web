import React, { Component } from 'react';
import Plot from 'react-plotly.js';

class TopChat extends Component {
    state = {
        topChat: [],
    }

    callApi = () => {

        fetch('http://127.0.0.1:8000/api' + this.props.match.url)
          
        .then(res => res.json())

        .then(json => this.setState({
            topChat: json,          
        }));  
    }

    componentDidMount() {
    
        this.callApi();
    
    }

    render() {
        const { topChat } = this.state;
        console.log(this.props.match.url);

        const wordlist = topChat.map((keyword) => (
            <tr> 
                <td>{keyword.rank}</td> 
                <td>{keyword.word}</td> 
                <td>{keyword.count}</td> 
                <td>{parseInt(keyword.appearance_time1/3600)}:{parseInt(keyword.appearance_time1%3600/60)}:{keyword.appearance_time1%60}</td> 
                <td>{parseInt(keyword.appearance_time2/3600)}:{parseInt(keyword.appearance_time2%3600/60)}:{keyword.appearance_time2%60}</td> 
                <td>{parseInt(keyword.appearance_time3/3600)}:{parseInt(keyword.appearance_time3%3600/60)}:{keyword.appearance_time3%60}</td> 
                <td>{parseInt(keyword.appearance_time4/3600)}:{parseInt(keyword.appearance_time4%3600/60)}:{keyword.appearance_time4%60}</td> 
                <td>{parseInt(keyword.appearance_time5/3600)}:{parseInt(keyword.appearance_time5%3600/60)}:{keyword.appearance_time5%60}</td> 
            </tr> 
        ))

        const {params} = this.props.match;
        console.log(params.value);
        console.log('?');
        return (
            <html>         
                <body>
        

                        scrolling="no" 
                    <div id="keywordChart">
                        <h3> 등장 빈도가 가장 높은 단어 5개를 보여줍니다!</h3>        
                        <h6> time을 클릭하면 영상이 해당 구간으로 이동하여 재생됩니다.</h6>
                        <br></br>
                        <table border="1">
                            <tbody>
                                <tr align ="center">
                                    <td width="50"> rank </td>
                                    <td width="150"> keyword </td>
                                    <td width="80"> count </td>
                                    <td width="150"> time1 </td>
                                    <td width="150"> time2 </td>
                                    <td width="150"> time3 </td>
                                    <td width="150"> time4 </td>
                                    <td width="150"> time5 </td>
        
                                </tr>
                                {wordlist}
                            </tbody>
                        </table>
           
                              
                    </div>
                    
                </body>
                
            </html>
        );
    }
}

  export default TopChat;