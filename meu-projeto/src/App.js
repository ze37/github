import React from 'react';
import './App.css';
import HelloWorld from './components/HelloWorld';
import SeyMyName from './components/SeyMyName';
import Pessoa from './components/pessoa';


const App = ()=> (

      < div className = "App" >
        
        <HelloWorld />
        <SeyMyName nome="zeneto" />
        <Pessoa nome="zeneto" idade="40" proficao="progamador" foto="https://via.placeholder.com/150"/>
        </div >
        
  )


export default App;
