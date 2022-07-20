//
//  ViewController.swift
//  MaskDetector
//
//  Created by R Albani on 01/03/2022.
//

import UIKit
import FirebaseStorage
import FirebaseDatabase

class ViewController: UIViewController {
    
    @IBOutlet var lockBtn: UIButton!
    @IBOutlet var UnlockBtn: UIButton!
    @IBOutlet var imageview: UIImageView!
    
    private let dataBase = Database.database().reference()
    private let storage = Storage.storage().reference()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        lockBtn.layer.cornerRadius = 10
        UnlockBtn.layer.cornerRadius = 10
        
        dataBase.observe(.childChanged) { (snapshot) in
            guard let value = snapshot.value as? String else{
                return print("error")
            }
            let url = URL(string: value)
            if let data = try? Data(contentsOf: url!){
                self.imageview.image = UIImage(data: data)
            }
        }
    }
    @IBAction func lockPressed(){
        guard let url = URL(string:"http://172.20.10.3/LED=OFF")
            else {return}
        
        var request = URLRequest(url:url)
        request.httpMethod = "POST"
        
        let session = URLSession.shared
        session.dataTask(with:request)
    }

    @IBAction func UnlockPressed(){
        guard let url = URL(string:"http://172.20.10.3/LED=ON")
            else {return}
        
        var request = URLRequest(url:url)
        request.httpMethod = "POST"
        
        let session = URLSession.shared
        session.dataTask(with:request)
    }


}

