import React, {Fragment} from 'react';
import axios from 'axios';

class AddActor extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      name: '',
      age: 0,
      gender: 'male'
    };
  }

    handleInputChange = (event) => {
      this.state[event.target.name] = event.target.value
    }

    create_actor = (event) => {
        event.preventDefault()
        axios.post(`http://localhost:8000/actors/`,{ 
          name: this.state.name,
          age: this.state.age,
          gender: this.state.gender
         })
          .then(res => {
            console.log(res)
            alert("Actor create")
        }).catch(error => {
          if (error.response.status === 400){
            alert("This actor exist")
        }
      })
    }

    render(){

    return (
        <Fragment>
            <h1>Create Actor</h1>
            <form className="row" onSubmit={this.create_actor}>
                <div className="col-md-3">
                    <label>Enter name:
                    <input type="text" placeholder="Name" className="form-control" onChange={this.handleInputChange} name="name"></input></label>
                </div>
                <div className="col-md-3">
                    <label>Enter age:
                    <input type="number" placeholder="Age" className="form-control" onChange={this.handleInputChange} name="age"></input></label>
                </div>
                <div className="col-md-3">
                    <label>Select gender:
                    <select  onChange={this.handleInputChange} name="gender">
                      <option value="male">male</option>
                      <option value="female">female</option>
                    </select></label>
                </div>
                <button type="submit" className="btn btn-primary">Enviar</button>
            </form>
        </Fragment>
    );
    }
}
 
export default AddActor;