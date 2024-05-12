import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProxyService {

  BASE_URL = 'http://127.0.0.1:5500/';

  constructor(private http: HttpClient) { }

  // function to call to the Python backend (Night Guard Proxy)
  checkKeepAlive() {
    return this.http.get(this.BASE_URL + 'proxy_monitor')
  }
}
