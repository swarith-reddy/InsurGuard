import React from 'react'
import NavLink from 'react-router-dom'

function Hurricane() {
    function req(state) {
        return "hello"
    }
    return(
        <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
            <h1>
                Hurricane Insurance
            </h1>
        <label>
            State Abbreviation:
        </label>
        <input type="field" name="state"/>
        <input type="submit" value="submit" onSubmit={req()}/>
        </div>
    )
}

export default Hurricane