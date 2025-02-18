import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appBar(context),
       body: Column(
         children: [
           Container(
             margin: EdgeInsets.only(top: 40, left: 20, right: 20),
            decoration: BoxDecoration(
              boxShadow:[
                BoxShadow(
                  color: Colors.black.withOpacity(0.11),
                  blurRadius: 2,
                  spreadRadius: 0.0
                )
              ]
            ),
            child: TextField(
             decoration: InputDecoration(
               filled: true,
               fillColor: Colors.white,
               contentPadding: EdgeInsets.all(15),
               prefixIcon:Padding(padding: const EdgeInsets.all(12),
                 child: SvgPicture.asset('assets/icons/Search.svg'),
               ),
               suffixIcon:Padding(padding: const EdgeInsets.all(12),
                 child: SvgPicture.asset('assets/icons/Filter.svg'),
               ),
               border: OutlineInputBorder(
                 borderRadius: BorderRadius.circular(11),
                 borderSide: BorderSide.none
               ),
             ),
           ),
           )
         ],
       ),
    );
  }

  AppBar appBar(BuildContext context) {
    return AppBar(
      title: Text(
        'Breakfast',
        style: TextStyle(
          color: Colors.black,
          fontSize: 25,
          fontWeight: FontWeight.bold,
        ),
      ),
      centerTitle: true,

      // Leading with GestureDetector
      leading: GestureDetector(
        onTap: () {
          // Handle back button press
          Navigator.pop(context);
        },
        child: Container(
          margin: EdgeInsets.all(10),
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: Color(0xffF7F8F8),
            borderRadius: BorderRadius.circular(10),
          ),
          child: SvgPicture.asset(
            'assets/icons/Arrow - Left 2.svg',
            height: 25,
            width: 25,
          ),
        ),
      ),

      // Actions with GestureDetector
      actions: [
        GestureDetector(
          onTap: () {
            // Handle dots menu tap
            print("Dots menu tapped");
          },
          child: Container(
            margin: EdgeInsets.all(10),
            alignment: Alignment.center,
            width: 37,
            decoration: BoxDecoration(
              color: Color(0xffF7F8F8),
              borderRadius: BorderRadius.circular(10),
            ),
            child: SvgPicture.asset(
              'assets/icons/dots.svg',
              height: 5,
              width: 5,
            ),
          ),
        ),
      ],
    );
  }
}
