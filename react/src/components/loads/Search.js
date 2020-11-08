import React, { Component } from 'react';
import Header from '../layout/Header';
import SelectChapter from './SelectChapter';
import selectchapter from './SelectChapter';

class Search extends Component {
    constructor(props) {
		super(props);
		this.state = {
			value: ''
		};
		
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	}
	
	handleChange(event){
		this.setState({value: event.target.value});
	}
	
	handleSubmit(event) {
        event.preventDefault();
        this.props.history.push('/selectchapter'+'/'+this.state.value)
    }

    render() {

        return (
            <html>
                <Header></Header>
                <header>
                    <h1 id= "servicename">유튜브 하이라이트 추출</h1>
                    <h4 id= "servicedsc"> 원하는 트위치 생방송 영상의 하이라이트를 추출해보세요! </h4>
                </header>

                <form action="/selectchapter" method="POST" onSubmit={this.handleSubmit}>
                    <input type="text" name="url" id="urlform" placeholder="원하는 트위치 영상의 url을 입력하세요" value={this.state.value} onChange={this.handleChange}/>
                    <input type ="submit" id="submit" value="검색" />
                </form>
               
            </html>
        );
    }
}

  export default Search;