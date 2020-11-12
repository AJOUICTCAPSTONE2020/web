import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import ChatFlow from "./stat/ChatFlow"
import AudioFlow from "./stat/AudioFlow"
import Sentiment from "./stat/Sentiment"
import TopChat from "./stat/TopChat"
import Header from '../layout/Header';
class Statistics extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value:'',
        };

    }


    render() {
        const {params} = this.props.match;
        return (
            <html>
                <Header></Header>
                <body>
                    <div id="stat">
                    <h4 id="statcdsc"> 확인할 통계를 선택하세요!</h4>
                        <Router>
                            <ul id="statList">
                                <Link to="/TopChat">
                                <button class="ChapterButton">Top 5 Chat</button>
                                </Link>
                                <Link to="/ChatFlow">
                                <button class="ChapterButton">Chat Flow</button>
                                </Link>
                                <Link to="/AudioFlow">
                                <button class="ChapterButton">Audio Flow</button>
                                </Link>
                                <Link to="/Sentiment">
                                <button class="ChapterButton">Sentiment Analysis</button>
                                </Link>
                            </ul>
                            <hr />
                            <main>
                                <Switch>
                                <Route exact path="/TopChat" component={TopChat} />
                                <Route path="/ChatFlow" component={ChatFlow} />
                                <Route path="/AudioFlow" component={AudioFlow} />
                                <Route path="/Sentiment" component={Sentiment} />
                                </Switch>
                            </main>
                        </Router>
                    </div>
                    
                </body>
                
            </html>
        );
    }
}

  export default Statistics;