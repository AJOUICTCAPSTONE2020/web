import React, { Component } from 'react';
import Plot from 'react-plotly.js';

class ChatFlow extends Component {
    constructor(props) {
        super(props);
        this.state = {
            chats: [],
        }
    }
 
    callApi = () => {

        fetch("http://127.0.0.1:8000/api/chatFlow/1")
          
        .then(res => res.json())

        .then(json => this.setState({
            chats: json,
        }));
    }

    componentDidMount() {
    
        this.callApi();
    
    }
    
    render() {
        const { chats } = this.state;
        const x=[];
        const y=[];
        for (var i in chats){
            x.push(chats[i].time)
        }
        
        for (var i in chats){
            y.push(chats[i].num_of_chat)
        }
   

        return (
            <html>         
                <body>

                    <Plot 
                        data={[
                            {
                                x:x,
                                y:y,
                                type: 'scatter',
                                mode : 'lines',
                                marker: {color:'#01A9DB'},
                            },
    
                        ]}
             
                    />
                </body>
                
            </html>
        );
    }
}

  export default ChatFlow;