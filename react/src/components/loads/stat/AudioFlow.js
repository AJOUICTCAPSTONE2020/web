import React, { Component } from 'react';
import Plot from 'react-plotly.js';
class AudioFlow extends Component {
    constructor(props) {
        super(props);
        this.state = {
            audio: [],
        }
    }

    
    callApi = () => {

        fetch("http://127.0.0.1:8000/api/audioFlow/1")
          
        .then(res => res.json())

        .then(json => this.setState({
            audio: json,
            
        }));

        
    }
    
      
    
      componentDidMount() {
    
        this.callApi();
    
      }
    
    render() {
        const { audio } = this.state;
        const x=[];
        const y=[];
        for (var i in audio){
            x.push(audio[i].time)
            console.log(audio)
            console.log(i)
        }
        for (var i in chats){
            y.push(audio[i].decibel)
        }

        return (
            <html>         
                <body>
                    
                    <Plot 
                        data={[
                            {
                                x:x1,
                                y:y1,
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

  export default AudioFlow;