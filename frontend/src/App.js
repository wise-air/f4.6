import './App.css';
import axios from 'axios';
import React from 'react';


class App extends React.Component{
  state = { details: [],}

  componentDidMount(){
    let data;
    axios.get('http://127.0.0.1:8000/api')
    .then(res =>{
      data = res.data;
      this.setState({
        details: data
      });
    })
    .catch(err =>{
      console.log(err);
    })
  }
  render() {
    return (
      <div>
        <header>Кулинарные рецепты</header>
        <hr></hr>
        {this.state.details.map((output, id) => (
         <div key={id}>
          <div>
            <h2> {output.title}</h2>
            <p>{output.description}</p>
            <p>{output.created_at}</p>
            <p>{output.updated_at}</p>
            </div>
         </div> 
        ))}
        </div>
    )
  }
}

export default App;
