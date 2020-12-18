import React, { useState, useContext } from 'react'
import styles from './registration.module.scss'
import Button from 'components/Button/Button'
import { gatewayApi } from 'api'
import AuthContext from 'context/AuthContext'
import ReCAPTCHA from "react-google-recaptcha";

import {useHistory } from "react-router-dom";

//this container defines the view of /registration endpoint
function Registration(){
    const SITE_KEY = "6Legv9sZAAAAALOPrMucKaKp29RFYWaWswPLuyQw";
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('') 
    const [conf_password, setConfPassword]=useState('')
    const [registerError, setRegisterError] = useState('')
    const [captcha, setCaptcha] = useState();    
    const { setRegistered } = useContext(AuthContext)
    const history = useHistory()
   
    
    function handleChange(value) {       
        setCaptcha(value)
      }
      const validate = (email) => {
        var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
        return pattern.test(String(email).toLowerCase())
    }

      const onUsernameChange = e => {
        setUsername(e.target.value)
      }
      const onPasswordChange = e => {
        setPassword(e.target.value)
      }
      const onConfPasswordChange = e =>{
          setConfPassword(e.target.value)
      }
    
      const register = async ()=>{
          try {          
            let jsonData={'email':username, 'password':password, 'captcha':captcha}           
            const response=await gatewayApi.post('/users/open', jsonData)
            if (response.data['status_code']===200){
             
                setRegistered('Your registration was successfull!');
                history.push('/login')
            }else{
                setRegisterError(response.data.body['detail'])
             
            }
        } catch (error){
            console.log(error)
        }
      }
      
      const onSignup = e =>{
       if (username===''){
           setRegisterError('Please enter your email')
        }else if(!validate(username)){
            setRegisterError('The email your entered is invalid. Please enter a valid email.')
       }else if (password===''|| conf_password===''){
        setRegisterError('Please enter and confirm your password.')
       }else  if (password!==conf_password){
            setRegisterError('Password and Confirm Password do not match.')
       }else if (!captcha){
        setRegisterError('Please confirm that you are not a robot.')
       }else{          
            register();
       }       
    }
    const onLogin = e =>{
        history.push('/login')
    }

   
    return (
     
        <div className={styles.background}>
            <div  className={styles.backgroundImage}>
                <h1>Differential<br></br>Diagnostics</h1>
                <h3>your personal symptoms checker</h3>
                <div className={styles.registrationBox}>
                    <h2>Sign up</h2>
                    <p>Please enter the required data</p>
                    <p className={styles.error}>{registerError}</p>    
                    <div className={styles.formArea}>
                        <input type='text' id='email' placeholder='Email' onChange={onUsernameChange} value={username} />
                        <form>
                        <input type='password' id='password' placeholder='Password' onChange={onPasswordChange} value={password} autoComplete="on" />
                        <input type='password' id='password_confirm' placeholder='Confirm Password' onChange={onConfPasswordChange} value={conf_password} autoComplete="on"  />
                        </form>
                        <ReCAPTCHA
                            style={{ display: "inline-block" }}
                                         
                            sitekey={SITE_KEY}
                            onChange={handleChange}                         
                        />
                        <Button
                        label="SIGN UP"
                        type="submit"
                        size="sm"
                        onClick={onSignup}
                        />
                       
                        </div>
                        <div style={{textAlign:'center'}}>          
                            <button className={styles.link} onClick={onLogin}>Login</button>          
                        </div>                
                </div>
            </div>
        </div>
        
    )
}

export default Registration