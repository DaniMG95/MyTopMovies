import React, {Fragment} from 'react';
import axios from 'axios';

class Movies extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
        actors: '',
        movies:[],
        movies_find:[],
        DataisLoaded: false
    };
    }


    componentDidMount() {
      this.get_movies()
    }


    get_movies = () => {
      axios.get(`http://localhost:8000/movies/`)
        .then(res => {
          this.setState({movies: res.data, DataisLoaded: true});
          console.log(res.data)
      })
    }


    handleInputChange = (event) => {
      this.state[event.target.name] = event.target.value
    }

    search_movie = (event) => {
      event.preventDefault()
        axios.get(`http://localhost:8000/performances/`,{ params: { actors: this.state.actors } })
          .then(res => {
            this.setState({movies: res.data})
        }).catch(error => {
          if (error.response.status === 400){
          alert("Some actors not exists")
        }
        })
    }



  render() {

    const { DataisLoaded, movies } = this.state;
    if (!DataisLoaded){
      return <div>
            <h1> Pleses wait some time.... </h1> </div> ;
    }
    return (
        <Fragment>
            <h1>Show Movies</h1>
            <form className="row" onSubmit={this.search_movie}>
                <div className="col-md-3">
                    <label>Search Movies:
                    <input type="text" placeholder="Actor1,Actor2" className="form-control" onChange={this.handleInputChange} name="actors"></input></label>
                </div>
                <button type="submit" className="btn btn-primary">Find</button>

            </form>

            <ul>
              {movies.map((movie) => <li>Title : {movie.title} | Category : {movie.category} | Cast : {movie.cast.map((cast) => cast + ' , ')} </li>)}
              
            </ul>
        </Fragment>
    );
  }
 
} 
export default Movies;