import React, {Component} from 'react';

export class Upload extends Component {
    constructor(props) {
        super(props)
        this.state = {
            image: undefined,
            title: ''
        }
        this.handleUpload = this.handleUpload.bind(this)
        this.handleImage = this.handleImage.bind(this)
        this.handleTitle = this.handleTitle.bind(this)
    }

    handleImage(event) {    
        console.log(event.target.files)
        this.setState({image: event.target.files[0]})
    }

    handleUpload(event) {
        if (!!this.state.image) {
            const form = new FormData()
            form.append('new_image', this.state.image)
            form.append('title', this.state.title)
            fetch(`${this.props.env.api}/images/`,
                {
                    method: 'POST',
                    body: form
                }
            ).then(_ => alert("Image uploaded!"))
        }
    }

    handleTitle(event) {
        this.setState({title: event.target.value})
    }

    render() {
        return (
            <form>
                <label for="title">Title: </label>
                <input type="text" name="title" onChange={this.handleTitle} />
                <input type="file" name="file" accept=".jpg" onChange={this.handleImage} />
                <input type="button" value="Upload" onClick={this.handleUpload} />
            </form>
        )
    }


}