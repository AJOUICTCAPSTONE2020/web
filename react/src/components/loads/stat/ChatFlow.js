import React, { Component } from 'react';
import Plot from 'react-plotly.js';
//from '../../../../../youha/models' import ChatFlow;
import axios from 'axios';

class ChatFlow extends Component {
    state={
        id:'',
        time:'',
        num_of_chat:''
    }

    
    callApi = () => {

        fetch("http://127.0.0.1:8000/api/chatFlow")
          
        .then(res => res.json())

        .then(json => {
            this.setState({ 
                id: json[2].id, time:json[2].time ,num_of_chat:json[2].num_of_chat
            });

        })
    
    }
    
      
    
      componentDidMount() {
    
        this.callApi();
    
      }
    
      

    render() {
        return (
            <html>         
                <body>
                <h3>{this.state.id}{this.state.time}{this.state.num_of_chat}</h3>
                    
                    <Plot 
                        data={[
                            {
                                x:[2,4,5,6],
                                y: [1,2,3,4],
                                type: 'scatter',
                                mode : 'lines',
                                marker: {color:'red'},
                            },
    
                        ]}
             
                    />
                </body>
                
            </html>
        );
    }
}

  export default ChatFlow;