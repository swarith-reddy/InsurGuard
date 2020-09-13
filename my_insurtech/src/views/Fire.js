import React from 'react'
import axios from 'axios'
import NavLink from 'react-router-dom'

function Fire() {
    function req(state) {
        axios.get
    }
    return(
        <div className="object-center">
            <label>
                State Abbreviation:
            </label>
            <input type="field" name="state"/>
            <input type="submit" value="submit" onSubmit={req()}/>
        </div>
    )
}

export default Fire