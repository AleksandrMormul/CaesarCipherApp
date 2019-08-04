import React, { Component } from 'react';

export default class CipherForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      content_encode: '',
      content_decode: '',
      shift: '',
    };
  }

  onSubmit() {
    fetch('/api/', {
      body: JSON.stringify(this.state),
      cache: 'no-cache',
      credentials: 'same-origin',
      headers: {
        'content-type': 'application/json',
      },

      method: 'POST',
      mode: 'cors',
      redirect: 'follow',
      referrer: 'no-referrer',
    });
  }

  getResult() {
    setTimeout(() => this.setState({ position: 1 }), 9000);
    fetch('/api/')
      .then(response => response.json())
      .then((apiJson) => {
        this.setState({ content_decode: apiJson.content_decode });
      });
  }


  render() {
    const v = () => {
      this.onSubmit();
    };

    const res = () => {
      this.getResult();
    };
    return (
      <form onSubmit={this.onSubmit.bind()}>
        <div className="row">
          <div className="col">
            <textarea onChange={e => this.setState({ content_encode: e.target.value })} name="content_decode" className="form-control rounded-0 w-75 p-3" id="exampleFormControlTextarea1" rows="10" placeholder="Input text" />
          </div>
          <div className="row">
            <div className="col mx-md-n5">
              <button onClick={v} type="button">Encode</button>
            </div>
            <div className="col mx-md-n5">
              <button onClick={res} type="button">Result</button>
            </div>
            <div className="col">
              <div className="input-group mb-2 mr-sm-2">
                <div className="input-group-prepend">
                  <div className="input-group-text">Shift</div>
                </div>
                <input onChange={e => this.setState({ shift: e.target.value })} name="shift" type="text" className="form-control" id="inlineFormInputGroupUsername2" placeholder="shift text" />
              </div>
            </div>
          </div>
          <div className="col">
            <textarea value={this.state.content_decode} onChange={e => this.setState({ content_decode: e.target.value })} name="content_decode" className="form-control rounded-0 w-75 p-3" rows="10" placeholder="Encoded text" />
          </div>
        </div>
      </form>
    );
  }
}
