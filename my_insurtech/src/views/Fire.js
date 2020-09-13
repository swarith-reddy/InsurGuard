import React from 'react'
import axios from 'axios'
import NavLink from 'react-router-dom'

function Fire() {
    function req(state) {
        return "hello"
    }
        return (
            <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', height: '100vh'}}>
                <h1>
                    Fire Insurance
                </h1>
            <label>
                State Abbreviation:
            </label>
            <input type="field" name="state"/>
            <input type="submit" value="submit" onSubmit={req()}/>
            </div>
          );
}

export default Fire