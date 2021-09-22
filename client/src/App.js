import logo from './logo.svg';
import './App.css';
import {Query} from './componenets/Query'
import {Upload} from './componenets/Upload' 

function App() {

  const ENV = {
    api: "http://localhost:5000"
  }

  return (
    <div>
      <h1>DaGallery</h1>
      <h3>A place to remember your world!</h3> 
      <h2>Upload An Image Here!</h2>
      <Upload env={ENV}></Upload>
      <h2>Get Your Images Here!</h2>
      <Query env={ENV}></Query>
    </div>
  );
}

export default App;
