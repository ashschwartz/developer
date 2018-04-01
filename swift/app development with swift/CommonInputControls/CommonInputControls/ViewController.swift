//
//  ViewController.swift
//  CommonInputControls
//
//  Created by Ash Schwartz on 3/31/18.
//  Copyright © 2018 Ash Schwartz. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var toggle: UISwitch!
    @IBOutlet weak var slider: UISlider!
    @IBOutlet weak var button: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        button.addTarget(self, action: #selector(buttonTapped(_:)), for: .touchUpInside)
    }

    
    @IBAction func buttonTapped(_ sender: UIButton) {
        print("Button was tapped!")
        
        if toggle.isOn {
            print("The switch is ON.")
        } else {
            print("The switch is OFF.")
        }
        
        print("The slider is set to \(slider.value).")
    }
    
    @IBAction func switchToggled(_ sender: UISwitch) {
    }
    
    @IBAction func sliderValueChanged(_ sender: UISlider) {
    }

    @IBAction func keyboardReturnKeyTapped(_ sender: UITextField) {
        if let text = sender.text {
            print(text)
        }
    }
    
    @IBAction func textChanged(_ sender: UITextField) {
        if let text = sender.text {
            print(text)
        }
    }
    
    @IBAction func respondToTapGesture(_ sender: UITapGestureRecognizer) {
        let location = sender.location(in: view)
        print(location)
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

