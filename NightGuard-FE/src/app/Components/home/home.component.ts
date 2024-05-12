import { Component } from '@angular/core';
import { ProxyService } from '../../Services/proxy.service';
import { CommonModule } from '@angular/common';
import { result } from '../../Models/result';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  constructor(private proxyService: ProxyService) {}

  // global variables
  result: result = new result;

  // function to call the "CheckKeepAlive" function in the proxy service
  checkKeepAlive() {
    this.proxyService.checkKeepAlive().subscribe((result: any) => {
        console.log(result)
    })
  }
}
