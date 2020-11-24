import React, { Component } from 'react';
import Header from '../layout/Header';

class AnalysisRecord extends Component {
    constructor(props) {
		super(props);
		this.state = {
            records:[],
            streamers:[],
        };

    }

    callApi1 = () => {

        fetch('http://127.0.0.1:8000/api/analysis')
        

        .then(res => res.json())

        .then(json => this.setState({
            records: json,
        }));
        
    }

    
    // callApi2 = () => {

    //     fetch('http://127.0.0.1:8000/api/streamer')
        

    //     .then(res => res.json())

    //     .then(json => this.setState({
    //         streamers: json,
    //     }));
        
    // }
    componentDidMount() {

        this.callApi1();
        // this.callApi2();
    

    }

    render() {
        const recordlist = this.state.records.map((keyword) => (
            <tr> 
                <td height="30">{keyword.title}</td>
                <td><a href="#">{keyword.name}</a></td>
                <td>{keyword.date}</td>
            </tr> 
        ))


        return (
            <html>
                <Header></Header>
                
                <body>
                    <div id="MyAnalysis">
                        <h4> 분석 기록 </h4>
                        <h6> 스트리머를 클릭하면 해당 스크리머의 기록만 모아볼 수 있습니다.</h6>
                        <table id="recordtable" border="2">
                            <tbody>
                                <tr align="center">
                                    <td width="400" height="50"> Title. </td>
                                    <td width="150"> Stramer. </td>
                                    <td width="150"> Date </td>
        
                                </tr>
                                {recordlist}
                            </tbody>
                        </table> 

                    </div>
         
                </body>               
            </html>
        );
    }
}
   



export default AnalysisRecord;
  