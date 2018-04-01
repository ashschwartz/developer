//
//  ViewController.swift
//  Two Buttons
//
//  Created by Ash Schwartz on 3/31/18.
//  Copyright © 2018 Ash Schwartz. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var textLabel: UILabel!
    @IBOutlet weak var textField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    @IBAction func setTextButtonTapped(_ sender: UIButton) {
        textLabel.text = textField.text
    }
    
    @IBAction func clearTextButtonTapped(_ sender: UIButton) {
        textField.text = ""
        textLabel.text = ""
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

