import { useContext, useEffect } from 'react'
import AuthContext from 'context/AuthContext'
import {useHistory } from "react-router-dom";
import { gatewayApi } from 'api'

export default function Logout() {
    const { setIsAuthenticated } = useContext(AuthContext)
    const history = useHistory()

    useEffect(() => {
        gatewayApi.post('/logout').then(response => {
            if (response.data['status_code'] === 200) {
                setIsAuthenticated(false)              
                history.push('/login')
            }
        })
    })

    return null
}

