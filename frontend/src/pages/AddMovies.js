import React, {Fragment} from 'react';
import axios from 'axios';

class AddMovies extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
        title: '',
        category: '',
        gender: 'male',
        actors:[],
        actors_selected:[],
        DataisLoaded: false
    };
    }


    componentDidMount() {
      this.get_actors()
    }


    get_actors = () => {
      axios.get(`http://localhost:8000/actors/`)
        .then(res => {
          this.setState({actors: []})
          res.data.forEach(element => {
            this.state.actors.push(element.name)
          });
          this.setState({DataisLoaded: true});
      })
    }


    handleInputChange = (event) => {
      if (event.target.name === "actors_selected"){
        let value = Array.from(event.target.selectedOptions, option => option.value);
        this.setState({actors_selected: value});
      }
      else{
        this.state[event.target.name] = event.target.value
      }
    }

    
    create_movie = (event) => {
      event.preventDefault()
        axios.post(`http://localhost:8000/movies/`,{ 
          title: this.state.title,
          category: this.state.category,
          cast: this.state.actors_selected
         })
          .then(res => {
            console.log(res)
            alert("Movie create")
        }).catch(error => {
          if (error.response.status === 400){
          alert("This movie exist")
        }
      })
    }



  render() {

    const { DataisLoaded, actors } = this.state;
    if (!DataisLoaded){
      return <div>
            <h1> Pleses wait some time.... </h1> </div> ;
    }
    return (
        <Fragment>
            <h1>Create Movie</h1>
            <form className="row" onSubmit={this.create_movie}>
                <div className="col-md-3">
                    <label>Enter title:
                    <input type="text" placeholder="Title" className="form-control" onChange={this.handleInputChange} name="title"></input></label>
                </div>
                <div className="col-md-3">
                    <label>Enter Category:
                    <input type="text" placeholder="Category" className="form-control" onChange={this.handleInputChange} name="category"></input></label>
                </div>
                <div className="col-md-3">
                    <label>Select actors:
                    <select  onChange={this.handleInputChange} name="actors_selected" id="actors_selected" multiple>
                    {actors.map((actor) => <option value={actor}>{actor}</option>)}
                    </select></label>
                </div>
                <button type="submit" className="btn btn-primary">Enviar</button>
            </form>
        </Fragment>
    );
  }
 
} 
export default AddMovies;