import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: const HomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final controller = TextEditingController();
  Map<String, dynamic>? result;

  Future<void> analyze() async {
    final response = await http.post(
      Uri.parse("http://127.0.0.1:8000/analyze"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"text": controller.text}),
    );

    setState(() {
      result = jsonDecode(response.body);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("AI Scam Detector")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: controller,
              maxLines: 3,
              decoration: const InputDecoration(
                hintText: "Введите сообщение (например: Вы выиграли 1 млн ₸)",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 12),
            ElevatedButton(onPressed: analyze, child: const Text("Analyze")),
            const SizedBox(height: 20),
            if (result != null) ...[
              Text("Risk score: ${result!["risk_score"]}%"),
              Text("Verdict: ${result!["verdict"]}"),
              const SizedBox(height: 8),
              ...List.from(result!["reasons"]).map((r) => Text("- $r")),
            ]
          ],
        ),
      ),
    );
  }
}
