import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root' 
})


export class DataService {

  constructor() { }
  /**
   * getString
   */
  public getString(str: string): Array<String> {
    let words = str.split(" ");
    return (words)
  }

}
