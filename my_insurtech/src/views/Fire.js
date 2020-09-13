import React from 'react'
import axios from 'axios'
import NavLink from 'react-router-dom'
import button from "../components/elements/Button"
import Button from '../components/elements/Button'

function Fire() {
    function req(state) {
        axios.post(
            "http://localhost:8000/",
            {
                "state":state
            }
        ).then(function (response) {
            document.getElementById("name").innerHTML = response 
        })
    }
        return (
            <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
                <h1>
                    Fire Insurance
                </h1>
            <label>
                State Abbreviation:
            </label>
            <input type="field" name="state" id="hullo" placeholder="Ex. CA" value="CA"/>
            <input type="submit" value="submit" onClick={req(document.getElementById("hullo").value)}/>
            <label id="name">Placeholders</label>
            </div>
          );
}

export default Fire