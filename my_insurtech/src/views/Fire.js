import React from 'react'
import axios from 'axios'
import NavLink from 'react-router-dom'
import button from "../components/elements/Button"
import Button from '../components/elements/Button'

function Fire() {
    function req(state) {
        const response = axios.get(
            "localhost:8000/?state="+state,
        )
        // document.getElementById("hello").innerHTML(response)
    }
    return(
        <div className="object-center">
            <form>
            <label>
                State Abbreviation:
            </label>
            <input type="field" name="state"/>
            <Button type="submit" value="submit" onSubmit={req()}/>
            </form>
            <label id="hello"></label>
        </div>
    )
}

export default Fire