import React from 'react'
import NavLink from 'react-router-dom'

function Flood() {
    return(
        <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
        <label>
            State Abbreviation:
        </label>
        <input type="field" name="state"/>
        <input type="submit" value="submit" onSubmit={req()}/>
        </div>
    )
}

export default Flood; 