import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import Home from './pages/Home'
import AddMovies from './pages/AddMovies';
import Movies from './pages/Movies';
import AddActor from './pages/AddActor';


const App = () => {
  return (
    <Router>
        <Routes>
          <Route exact path="/" element={<Home/>}/>
        </Routes>
        <Routes>
          <Route exact path="/addmovie" element={<AddMovies/>}/>
        </Routes>
        <Routes>
          <Route exact path="/movies" element={<Movies/>}/>
        </Routes>
        <Routes>
          <Route exact path="/addactor" element={<AddActor/>}/>
        </Routes>
    </Router>
  );
}


export default App;
