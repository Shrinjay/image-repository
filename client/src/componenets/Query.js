import {Images} from './Images'
import React, {Component} from 'react';

export class Query extends Component {
    constructor(props) {
        super(props)
        this.state = {
            user: '',
            title: '',
            city: '',
            country: '',
            object: '',
            images: null
        }
        this.handleUser = this.handleUser.bind(this)
        this.handleTitle = this.handleTitle.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.handleCity = this.handleCity.bind(this)
        this.handleCountry = this.handleCountry.bind(this)
        this.handleObject = this.handleObject.bind(this)
    }

    handleUser(event) {
        this.setState({user: event.target.value})
    }

    handleTitle(event) {
        this.setState({title: event.target.value})
    }

    handleObject(event) {
        this.setState({object: event.target.value})
    }

    handleCity(event) {
        this.setState({city: event.target.value})
    }

    handleCountry(event) {
        this.setState({country: event.target.value})
    }

    handleSubmit(event) {
        fetch(`${this.props.env.api}/images/?title=${this.state.title}&city=${this.state.city}&country=${this.state.country}&object=${this.state.object}`)
        .then(response => response.json())
        .then(images => this.setState({images: images}))
    }

    render() {
        return (
            <div>
                <form>
                    <label>Image Title: </label>
                    <input type="text" value={this.state.title} onChange={this.handleTitle} />
                    <br />
                    <label>Object in Image: </label>
                    <input type="text" value={this.state.object} onChange={this.handleObject} />
                    <br />
                    <label>City where image was taken</label>
                    <input type="text" value={this.state.city} onChange={this.handleCity} />
                    <br />
                    <label>Country where image was taken</label>
                    <input type="text" value={this.state.country} onChange={this.handleCountry} />
                    <br />
                    <input type="button" value="Submit" onClick={this.handleSubmit}/>
                </form>
                <br />
                <div style={{display: 'flex', flex: "0 0 25%", flexDirection: "column",
                  justifyContent:'center', alignItems:'center'}}>
                    {this.state.images === null ? null : <Images images={this.state.images} />}
                </div>
            </div>
        )
    }
}