import React from 'react';
import './App.css';
import CipherForm from './components/CipherForm';

const App = () => (
  <div className="App">
    <div className="App-header" />
    <div className="container">
      <div className="row">
        <div className="col-12 col-md-8">Caesar Cipher</div>
      </div>
      <CipherForm />
    </div>
  </div>
);

export default App;
