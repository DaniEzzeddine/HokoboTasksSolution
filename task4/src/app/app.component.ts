import { Component } from '@angular/core';
import { DataService } from "./data.service";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html' 
})

export class AppComponent  {
  values = '';
  data:DataService = new DataService;
  prevValue:string =""
  stringArr = []
  table:Object = {}
  onKey(event: any) {
    const input = event.target.value
    this.values = event.target.value
    setTimeout((val:string = input) => {

      if (val == event.target.value && val != this.prevValue){
        this.stringArr = this.data.getString(val);
        this.stringArr.forEach(element => {
          if (this.table.hasOwnProperty(element))
            this.table[element]++;
          else if (element != "")
            this.table[element] = 1;
        });

        console.log(this.table)
        this.table = {}
      }
      this.prevValue = val
    }, 450)
  }
}

