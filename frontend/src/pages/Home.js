import React from 'react'
import { Link } from "react-router-dom";


const Home = () => (
  <section className="Home">
    <h3>Hello to Movies</h3>
    <nav
        style={{
          borderBottom: "solid 1px",
          paddingBottom: "1rem"
        }}
      >
        <Link to="/addactor">addactor</Link> |{" "}
        <Link to="/addmovie">addmovie</Link> |{" "}
        <Link to="/movies">movies</Link>
      </nav>
  </section>
)

export default Home