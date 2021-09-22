import React, {Component} from 'react';

export class Images extends Component {
    constructor(props) {
        super(props)
    }

    getImages() {
        return this.props.images.map(image => {
            return (
            <div>
                <img style={{minWidth: '15%', maxWidth: '20%'}} src={image} />
            </div>
            )
        })
    }

    render() {
        return this.getImages()
    }
}